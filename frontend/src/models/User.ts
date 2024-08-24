export type User = {
    name?: string;
    email: string;
    password: string;
    is_active?: string;
    is_admin?: string;
}

export type Logged = User & {
    refresh: string;
    access: string;
}