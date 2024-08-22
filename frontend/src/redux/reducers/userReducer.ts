import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import {User} from "../../models/User"

export const authSlice = createSlice({
    name:"auth",
    initialState:{
        user: null as User | null,
    },
    reducers:{
        setUser:(state, action: PayloadAction<User>) => {
            state.user = action.payload
        }

    }
})

export const setUser = authSlice.actions

export default authSlice.reducer