// Estado Global del producto y acciones
// Created By. Ing Edward Acosta

import { defineStore } from 'pinia'
import api from '../services/api'

export const useProductStore = defineStore('product', {
    state: () => ({
        products: [],
        loading: false,
        error: null,
        productHistory: []
    }),

    actions: {
        async fetchProducts(search = '') {
            this.loading = true
            this.error = null
            try {
                const response = await api.get('/products/', {
                    params: { search }
                })
                this.products = response.data
            } catch (err) {
                this.error = err.response?.data?.detail || 'Error al cargar los productos'
                console.error(err)
            } finally {
                this.loading = false
            }
        },


        async createProduct(productData) {
            this.loading = true
            this.error = null
            try {
                await api.post('/products/', productData)
                await this.fetchProducts()
            } catch (err) {
                this.error = err.response?.data?.detail || 'Error al crear el producto'
                throw err
            } finally {
                this.loading = false
            }
        },


        async updateProduct(id, productData) {
            this.loading = true
            try {
                await api.put(`/products/${id}`, productData)
                await this.fetchProducts()
            } catch (err) {
                this.error = 'Error al actualizar el producto'
                throw err
            } finally {
                this.loading = false
            }
        },

        async toggleStatus(id) {
            try {
                await api.patch(`/products/${id}/status`)
                await this.fetchProducts()
            } catch (err) {
                this.error = 'Error al cambiar el estado'
                console.error(err)
            }
        },

        // (Soft Delete)
        async deleteProduct(id) {
            try {
                await api.delete(`/products/${id}`)
                await this.fetchProducts()
            } catch (err) {
                this.error = 'Error al eliminar el producto'
                throw err
            }
        }
    }
})