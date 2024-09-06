import { User, Logged } from "../models/User";
import { Category, Post, Comment, ImagePost } from "../models/Posts";
import { useApi } from "./api";

// User requests
export const createUser = async ({ name, email, password }: User) => {
    const response = await useApi<User>('users/signup', 'POST', { name, email, password }, false);
    return response;
}

export const login = async ({ email, password }: User) => {
    const response = await useApi<Logged>('users/login', 'POST', { email, password }, false);
    return response;
}

// Category requests
export const getCategories = async () => {
    const response = await useApi<Category[]>('categories', 'GET', {}, false);
    return response;
}

export const getCategoryById = async (id: number) => {
    const response = await useApi<Category>(`categories/${id}/`, 'GET', {}, false);
    return response;
}

export const createCategory = async ({ name }: Category) => {
    const response = await useApi<Category>('categories', 'POST', { name });
    return response;
}

export const updateCategory = async (id: number, { name }: Category) => {
    const response = await useApi<Category>(`categories/${id}/`, 'PUT', { name });
    return response;
}

export const partialUpdateCategory = async (id: number, data: Partial<Category>) => {
    const response = await useApi<Category>(`categories/${id}/`, 'PATCH', data);
    return response;
}

export const deleteCategory = async (id: number) => {
    const response = await useApi<null>(`categories/${id}/`, 'DELETE', {});
    return response;
}

// Post requests
export const getPosts = async () => {
    const response = await useApi<Post[]>('posts', 'GET', {}, false);
    return response;
}

export const getPostById = async (id: number) => {
    const response = await useApi<Post>(`posts/${id}/`, 'GET', {}, false);
    return response;
}

export const createPost = async (post: Post) => {
    const response = await useApi<Post>('posts', 'POST', post);
    return response;
}

export const updatePost = async (id: number, post: Post) => {
    const response = await useApi<Post>(`posts/${id}/`, 'PUT', post);
    return response;
}

export const partialUpdatePost = async (id: number, data: Partial<Post>) => {
    const response = await useApi<Post>(`posts/${id}/`, 'PATCH', data);
    return response;
}

export const deletePost = async (id: number) => {
    const response = await useApi<null>(`posts/${id}/`, 'DELETE', {});
    return response;
}

// Comment requests
export const getComments = async () => {
    const response = await useApi<Comment[]>('comments', 'GET', {}, false);
    return response;
}

export const getCommentById = async (id: number) => {
    const response = await useApi<Comment>(`comments/${id}/`, 'GET', {}, false);
    return response;
}

export const createComment = async (comment: Comment) => {
    const response = await useApi<Comment>('comments', 'POST', comment);
    return response;
}

export const updateComment = async (id: number, { content }: Comment) => {
    const response = await useApi<Comment>(`comments/${id}/`, 'PUT', { content });
    return response;
}

export const partialUpdateComment = async (id: number, data: Partial<Comment>) => {
    const response = await useApi<Comment>(`comments/${id}/`, 'PATCH', data);
    return response;
}

export const deleteComment = async (id: number) => {
    const response = await useApi<null>(`comments/${id}/`, 'DELETE', {});
    return response;
}

// ImagePost requests
export const getImages = async () => {
    const response = await useApi<ImagePost[]>('images', 'GET', {}, false);
    return response;
}

export const getImageById = async (id: number) => {
    const response = await useApi<ImagePost>(`images/${id}/`, 'GET', {}, false);
    return response;
}

export const createImage = async (imagePost: ImagePost) => {
    const response = await useApi<ImagePost>('images', 'POST', imagePost);
    return response;
}

export const updateImage = async (id: number, imagePost: ImagePost) => {
    const response = await useApi<ImagePost>(`images/${id}/`, 'PUT', imagePost);
    return response;
}

export const partialUpdateImage = async (id: number, data: Partial<ImagePost>) => {
    const response = await useApi<ImagePost>(`images/${id}/`, 'PATCH', data);
    return response;
}

export const deleteImage = async (id: number) => {
    const response = await useApi<null>(`images/${id}/`, 'DELETE', {});
    return response;
}
