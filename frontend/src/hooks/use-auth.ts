import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { api } from '@/lib/api'
import { AuthResponse, User } from '@/lib/api-types'

interface LoginData {
    email: string
    password: string
}

interface RegisterData {
    email: string
    password: string
    name: string
}

export function useAuth() {
    const queryClient = useQueryClient()

    const login = useMutation({
        mutationFn: async (data: LoginData): Promise<AuthResponse> => {
            const response = await api.post('/auth/login', data)
            return response.data
        },
        onSuccess: (data) => {
            localStorage.setItem('access_token', data.access_token)
            queryClient.setQueryData(['user'], data.user)
        },
    })

    const register = useMutation({
        mutationFn: async (data: RegisterData): Promise<AuthResponse> => {
            const response = await api.post('/auth/register', data)
            return response.data
        },
        onSuccess: (data) => {
            localStorage.setItem('access_token', data.access_token)
            queryClient.setQueryData(['user'], data.user)
        },
    })

    const logout = useMutation({
        mutationFn: async () => {
            await api.post('/auth/logout')
        },
        onSuccess: () => {
            localStorage.removeItem('access_token')
            queryClient.clear()
        },
    })

    const { data: user, isLoading } = useQuery({
        queryKey: ['user'],
        queryFn: async (): Promise<User> => {
            const response = await api.get('/auth/me')
            return response.data
        },
        enabled: !!localStorage.getItem('access_token'),
    })

    return {
        user,
        isLoading,
        isAuthenticated: !!user,
        login,
        register,
        logout,
    }
}