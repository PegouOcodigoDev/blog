import axios from "axios"

const BASE_URL ='http://172.26.3.93:8000/api'


export const useApi = async <TypeDataResponse>(
    endpoint: string,
    method: 'GET'|'POST'|'PUT'|'DELETE' = 'GET',
    data?: object,
): Promise<{
    data?: TypeDataResponse | null,
    detail: string
}> =>{

    try{
        const request = await axios(`${BASE_URL}/${endpoint}`,{
            method,
            data: method != 'GET' && data,
            params: method == 'GET' && data
        })

        return {
            data: request.data,
            detail: ''
        }

    }catch(e){
        return{
            data: null,
            detail: 'Deu ruim'
        }
    }
    
}
