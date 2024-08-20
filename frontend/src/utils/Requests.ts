import { User } from "../models/User"
import { useApi } from "./Api"

const signUp = async ({name, email, password}: User) => {
    const response = await useApi<User>('users/signup','POST', {name, email, password});
    return response;
}

export default signUp;