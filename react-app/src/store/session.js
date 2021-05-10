const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";

const setUser = (user) => ({
    type: SET_USER,
    payload: user
})

const removeUser = () => ({
    type: REMOVE_USER
})


export const authenticate = () => async dispatch => {
    const response = await fetch('/api/auth/', {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const user = await response.json();
    if (!user.errors) dispatch(setUser(user))
}

export const login = (email, password) => async dispatch => {
    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            password
        })
    });
    const user = await response.json();
    if (user.errors) {
        const err = new Error('Unauthorized')
        err.errors = user.errors;
        throw err;
    } else dispatch(setUser(user))
}


export const signUp = (username, email, password) => async dispatch => {
    const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username,
            email,
            password,
        }),
    });
    const user = await response.json();
    if (user.errors) {
        const err = new Error('Unauthorized')
        err.errors = user.errors;
        throw err;
    } else dispatch(setUser(user))
}

export const logout = () => async dispatch => {
    const response = await fetch("/api/auth/logout", {
        headers: {
            "Content-Type": "application/json",
        }
    });
     dispatch(removeUser());
};


const initialState = { user: null, loaded: false };

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_USER:
            return { ...state, user: action.payload, loaded: true };
        case REMOVE_USER:
            return { ...state, user: null, loaded: true };
        default:
            return state;
    }
}
