import axios, {AxiosError} from "axios";
import { ApiError } from "../models/ApiError";

const BASE_URL ='http://127.0.0.1:8000/api'


export const useApi = async <TypeDataResponse>(
    endpoint: string,
    method: 'GET'|'POST'|'PUT'|'DELETE' = 'GET',
    data?: object,
): Promise<{
    data?: TypeDataResponse | null,
    detail: string
}> =>{

    try{
        const request = await axios(`${BASE_URL}/${endpoint}`,{
            method,
            data: method != 'GET' && data,
            params: method == 'GET' && data
        })

        return {
            data: request.data,
            detail: ''
        }

    }catch(e){
        const error = e as AxiosError<ApiError>
        return{
            data: null,
            detail: error.response?.data.detail || error.message
        }
    }
    
}
