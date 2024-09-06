import { User } from "./User";

export type Category = {
    name: string;
}

export type Comment = {
    post: Post;
    author: User;
    content: string;
    created_at: string;
}

export type ImagePost = {
    post: Post;
    image: string;
}

export type Post = {
    category?: Category | null;
    author: User;
    title: string;
    slug: string;
    content: string;
    likes: number;
    status: "draft" | "published";
    comment_count: number;
}
