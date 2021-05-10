const GET_ALL_TAGS = 'tag/GET_ALL_TAGS'


const getTagsAction = (tags) => ({
  type: GET_ALL_TAGS,
  payload: tags
})


export const getTags = () => async (dispatch) => {
  const response = await fetch('/api/tags/')
  const data = await response.json()
  dispatch(getTagsAction(data.tags))
  return data.tags
}

const initialState = {};

export default function reducer(state = initialState, action) {
  switch (action.type) {
      case GET_ALL_TAGS:
          return { ...action.payload };
      default:
          return state;
  }
}
