import React from 'react';
import { useSelector} from 'react-redux'
import { NavLink } from 'react-router-dom';
import './Result.css'

const Result = (props) => {
  // console.log('CREATURE', creature
  const {id, name, description} = props.data
  const images = useSelector(state => state.image)
  const imageArr = []
  for (const image in images) {
    if (images[image].creature_id === id)
      imageArr.push(images[image])
  }

  return (
    <div className='spacer'>
      <div className='main__container'>
        <div className='result__container'>
          <NavLink to={`/creatures/${id}`} className='result__link'>
            <div className='info__container'>
              {imageArr.length > 0 &&
                <div className='result__thumbnail'><img className='result__thumbnail' src={imageArr[0].url}></img></div>
                }
                <div className='result__name'>{name}</div>
                <div className='result__description'>{description}</div>
              
            </div>
          </NavLink>
        </div>
      </div>
    </div>
  )
}

export default Result
