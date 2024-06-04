import axios from 'axios'

const apiURl = axios.create({
    baseURL: 'https://inventory-manager-bzro.onrender.com/inventory_manager/api/'
})

// Se dejan estas funciones como ejemplo
export const getAllRol = ()=> apiURl.get('/Rol/');


export const createRol= (rol) => apiURl.post("/", rol);