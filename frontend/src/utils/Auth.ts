const ACCESS_TOKEN_KEY = "access_token";
const REFRESH_TOKEN_KEY = "refresh_token";

export const handleGetAccessToken = () => localStorage.getItem(ACCESS_TOKEN_KEY);

export const handleGetRefreshToken = () => localStorage.getItem(REFRESH_TOKEN_KEY);

export const logOut = () => {
    localStorage.removeItem(ACCESS_TOKEN_KEY);
    localStorage.removeItem(REFRESH_TOKEN_KEY);
};