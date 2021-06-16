const GET_ALL_IMAGES = 'image/GET_ALL_IMAGES'
const CREATE_IMAGE = 'image/CREATE_IMAGE'

const getAllImagesAction = (images) => ({
  type: GET_ALL_IMAGES,
  payload: images
})

const createImageAction = (image) =>({
  type: CREATE_IMAGE,
  payload:image
})

export const getImages = () => async (dispatch) => {
  const response = await fetch('/api/images/')
  const data = await response.json()
  dispatch(getAllImagesAction(data.images))
  return data.images
}


export const createImage = (image) => async (dispatch) => {
  const response = await fetch ('/api/images', {
    method: 'POST',
    headers: {
      'Content-Type' : 'application/json'
    },
    body: JSON.stringify(image)
  })
  const data = await response.json()
  if (data.errors) {
    const err = new Error('Unauthorized')
    err.errors = data.errors;
    throw err;
} else
  dispatch(createImageAction(data))
  // console.log("DATA ------>", data)
  return data
}


const initialState = {};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_IMAGES:
            return { ...action.payload };
        case CREATE_IMAGE:
          const newImageState = {...state}
          newImageState[action.payload.id] = action.payload
          return newImageState
        default:
            return state;
      }
    }
