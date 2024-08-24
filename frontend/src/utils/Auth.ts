const ACCESS_TOKEN = localStorage.getItem("access_token");
const REFRESH_TOKEN = localStorage.getItem("refresh_token");

export const handleGetAccessToken = () => localStorage.getItem(ACCESS_TOKEN ?? "");

export const handleGetRefreshToken = () => localStorage.getItem(REFRESH_TOKEN ?? "");

export const logOut = () => {
    localStorage.removeItem(`${ACCESS_TOKEN}`);
    localStorage.removeItem(`${REFRESH_TOKEN}`)
}