const GET_ALL_FAVORITES = 'favorite/GET_ALL_FAVORITES'
const ADD_FAVORITE = 'favorite/ADD_FAVORITE'
const REMOVE_FAVORITE = 'favorite/REMOVE_FAVORITE'

const getFavoritesAction = (favorites) => ({
  type: GET_ALL_FAVORITES,
  payload: favorites
})

const addFavoriteAction = (favorite) => ({
  type: ADD_FAVORITE,
  payload: favorite
})

const removeFavoriteAction = (favorite) => ({
  type: REMOVE_FAVORITE,
  payload:favorite
})

export const getFavorites = () => async (dispatch) => {
  // console.log('Before')
  const response = await fetch('/api/favorites/')
  const data = await response.json()
  dispatch(getFavoritesAction(data.favorites))
  return data.favorites
}

export const addFavorite = (favorite) => async (dispatch) => {
  const response = await fetch ('/api/favorites/add/', {
    method: 'POST',
    headers: {
      'Content-Type' : 'application/json'
    },
    body: JSON.stringify(favorite)
  })
  const data = await response.json()
  if (data.errors) {
    const err = new Error('Unauthorized')
    err.errors = data.errors;
    throw err;
} else
  dispatch(addFavoriteAction(data))
  // console.log("DATA ------>", data)
  return data
}

export const removeFavorite = async (dispatch) => {
  const response = await fetch('/api/favorites/remove/', {
    method: 'DELETE',
  })
  const data = await response.json()
  if (data.errors) {
    const err = new Error('Unauthorized')
    err.errors = data.errors;
    throw err;
} else
  dispatch(removeFavoriteAction(data))
  // console.log("DATA ------>", data)
  return data
}

const initialState = {};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_FAVORITES:
            return { ...action.payload };
        case ADD_FAVORITE:
            const addFavoriteState = {...state}
            addFavoriteState[action.payload.id] = action.payload
            return addFavoriteState
        case REMOVE_FAVORITE:
            const removeFavoriteState = {...state}
            removeFavoriteState[action.payload.id].destroy()
            return removeFavoriteState
        default:
            return state;
    }
  }
