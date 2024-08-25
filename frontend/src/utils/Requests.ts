import { User, Logged } from "../models/User";
import { useApi } from "./api";

export const createUser = async ({name, email, password}: User) => {
    const response = await useApi<User>('users/signup','POST', {name, email, password}, false);
    return response;
}

export const login = async ({email, password}: User) => {
    const response = await useApi<Logged>('users/login', 'POST', {email, password}, false);
    return response;
}

