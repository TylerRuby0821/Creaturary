const GET_ALL_CREATURES = 'creature/GET_ALL_CREATURES'
const GET_CREATURE_BY_ID = 'creature/GET_CREATURE_BY_ID'
const GET_ALL_CREATURES_LORE = 'creature/GET_ALL_CREATURES_LORE'
const GET_ALL_CREATURES_AZ = 'creature/GET_ALL_CREATURES_AZ'
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
const getCreaturesAzAction = (creatures) => ({
  type: GET_ALL_CREATURES_AZ,
  payload: creatures
})
const getCreaturesCustomAction = (creatures) => ({
  type: GET_ALL_CREATURES_CUSTOM,
  payload: creatures
})
const createCreaturesAction = (creature) => ({
  type: CREATE_CREATURE,
  payload: creature
})


export const getCreatures = () => async (dispatch) => {
  console.log('Before')
  const response = await fetch('/api/creatures/')
  const data = await response.json()
  dispatch(getCreaturesAction(data.creatures))
  return data.creatures
}

export const getCreature = (id) => async (dispatch) => {
  const response = await fetch(`/api/creatures/${id}`)
  console.log("Im RESPONSE", response)
  const data = await response.json()
  console.log('IM DATA', data)
  dispatch(getCreatureByIdAction(data))
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
        default:
            return state;
    }
}
