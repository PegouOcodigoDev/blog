import axios, { AxiosError, AxiosResponse } from "axios";
import { ApiError } from "../models/ApiError";
import { handleGetAccessToken, handleGetRefreshToken } from "./auth";

const BASE_URL = "http://127.0.0.1:8000/api";

export const refreshAccessToken = async () => {
  const response = await axios.post(`${BASE_URL}/token/refresh/`, {refresh: handleGetRefreshToken()})
  return response.data.access_token;
}

export const useApi = async <TypeDataResponse>(
  endpoint: string,
  method: "GET" | "POST" | "PUT" | "DELETE" = "GET",
  data?: object,
  withAuth: boolean = true
): Promise<{
  data?: TypeDataResponse | null;
  detail: string;
}> => {
  const access_token = handleGetAccessToken();

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };

  if (access_token && withAuth) {
    headers["Authorization"] = `Bearer ${access_token}`;
  }

  try {
    const response: AxiosResponse<TypeDataResponse> = await axios({
      url: `${BASE_URL}/${endpoint}`,
      method,
      data: method !== "GET" ? data : undefined,
      params: method === "GET" ? data : undefined,
      headers,
    });

    return {
      data: response.data,
      detail: "",
    };
  } catch (error) {
    const axiosError = error as AxiosError<ApiError>;

    if(axiosError.response?.status === 401){
      try {
        const newAccessToken = await refreshAccessToken();
        localStorage.setItem("access_token", newAccessToken);

        headers["Authorization"] = `Bearer ${newAccessToken}`;

        const response: AxiosResponse<TypeDataResponse> = await axios({
          url: `${BASE_URL}/${endpoint}`,
          method,
          data: method !== "GET" ? data : undefined,
          params: method === "GET" ? data : undefined,
          headers,
        });

        return {
          data: response.data,
          detail: "",
        };
      } catch (refreshError) {
        return {
          data: null,
          detail: "Falha a renovar o token de acesso.",
        };
      }
    }

    return {
      data: null,
      detail: axiosError.response?.data.detail || axiosError.message,
    };
  }
};