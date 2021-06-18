const GET_ALL_FAVORITES = 'favorite/GET_ALL_FAVORITES'


const getFavoritesAction = (favorites) => ({
  type: GET_ALL_FAVORITES,
  payload: favorites
})


export const getFavorites = () => async (dispatch) => {
  // console.log('Before')
  const response = await fetch('/api/favorites/')
  const data = await response.json()
  dispatch(getFavoritesAction(data.favorites))
  return data.favorites
}

const initialState = {};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_FAVORITES:
            return { ...action.payload };
        default:
            return state;
    }
  }
