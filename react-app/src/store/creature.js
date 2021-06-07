const GET_ALL_CREATURES = 'creature/GET_ALL_CREATURES'
const GET_CREATURE_BY_ID = 'creature/GET_CREATURE_BY_ID'
const GET_ALL_CREATURES_LORE = 'creature/GET_ALL_CREATURES_LORE'
const GET_ALL_CREATURES_SEARCH = 'creature/GET_ALL_CREATURES_SEARCH'
const GET_ALL_CREATURES_CUSTOM = 'creature/GET_ALL_CREATURES_CUSTOM'
const CREATE_CREATURE = 'creature/CREATE_CREATURE'

const getCreaturesAction = (creatures) => ({
  type: GET_ALL_CREATURES,
  payload: creatures
})
const getCreatureByIdAction = (creature) => ({
  type: GET_CREATURE_BY_ID,
  payload: creature
})
const getCreaturesLoreAction = (creatures) => ({
  type: GET_ALL_CREATURES_LORE,
  payload: creatures
})
const getCreaturesSearchAction = (creatures) => ({
  type: GET_ALL_CREATURES_SEARCH,
  payload: creatures
})
const getCreaturesCustomAction = (creatures) => ({
  type: GET_ALL_CREATURES_CUSTOM,
  payload: creatures
})
const createCreatureAction = (creature) => ({
  type: CREATE_CREATURE,
  payload: creature
})


export const getCreatures = () => async (dispatch) => {
  // console.log('Before')
  const response = await fetch('/api/creatures/')
  const data = await response.json()
  dispatch(getCreaturesAction(data.creatures))
  return data.creatures
}
export const getCreaturesSearch = (search) => async (dispatch) => {
  // console.log('Before')
  const response = await fetch(`/api/creatures/${search}`)
  const data = await response.json()
  dispatch(getCreaturesSearchAction(data.creatures))
  return data.creatures
}

export const getCreaturesLore = () => async (dispatch) => {
  const response = await fetch('/api/creatures/lore')
  const data = await response.json()
  dispatch(getCreaturesLoreAction(data.creatures))
  return data.creatures
}
export const getCreaturesCustom = () => async (dispatch) => {
  const response = await fetch('/api/creatures/custom')
  const data = await response.json()
  dispatch(getCreaturesCustomAction(data.creatures))
  return data.creatures
}

export const getCreature = (id) => async (dispatch) => {
  const response = await fetch(`/api/creatures/${id}`)
  const data = await response.json()
  dispatch(getCreatureByIdAction(data))
  return data
}

export const createCreature = (creature) => async (dispatch) => {
  const response = await fetch ('/api/creatures/create', {
    method: 'POST',
    headers: {
      'Content-Type' : 'application/json'
    },
    body: JSON.stringify(creature)
  })
  const data = await response.json()
  if (data.errors) {
    const err = new Error('Unauthorized')
    err.errors = data.errors;
    throw err;
} else
  dispatch(createCreatureAction(data))
  // console.log("DATA ------>", data)
  return data
}

const initialState = {};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_CREATURES:
            return { ...action.payload };
        case GET_CREATURE_BY_ID:
            const newState = {...state}
            newState[action.payload.id] = action.payload
            return newState;
        case GET_ALL_CREATURES_LORE:
            const loreState = {...action.payload}
            return loreState
        case GET_ALL_CREATURES_CUSTOM:
            const customState = {...action.payload}
            return customState
        case GET_ALL_CREATURES_SEARCH:
            const searchState = {...action.payload}
            return searchState
        case CREATE_CREATURE:
            const newCreatureState = {...state}
            newCreatureState[action.payload.id] = action.payload
            return newCreatureState
        default:
            return state;
    }
}
