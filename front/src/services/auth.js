import config from "@/config.js";

export async function login(idUser, password) {
    const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            user: idUser,
            password: password,
        }),

    };


    const response = await fetch(`${config.AUTH_PATH}/login`, settings);
    return response
}

export async function signUp(idUser, password, name) {
    const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: idUser,
            user: name,
            password: password,
        }),

    };
    const response = await fetch(`${config.API_PATH}/user`, settings);
    return response
}

