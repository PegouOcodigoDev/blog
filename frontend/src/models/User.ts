export type User = {
    name?: string;
    email: string;
    password: string;
}

export type Logged = User & {
    refresh: string;
    access: string;
}