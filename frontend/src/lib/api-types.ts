// API response types
export interface ApiResponse<T> {
    data: T
    message?: string
}

export interface User {
    id: string
    email: string
    name: string
    created_at: string
    updated_at: string
}

export interface AuthResponse {
    access_token: string
    token_type: string
    user: User
}

// Add more types as needed