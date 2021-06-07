import React from 'react';
import { NavLink } from 'react-router-dom';
import './Result.css'

const Result = (props) => {
  // console.log('CREATURE', creature
  const {id, name, description} = props.data
  return (
    <div className='spacer'>
      <div className='main__container'>
        <div className='result__container'>
          <NavLink to={`/creatures/${id}`} className='result__link'>
            <div className='result__thumbnail'>{/*Thumbnail*/}</div>
            <div className='result__name'>{name}</div>
            <div className='result__description'>{description}</div>
          </NavLink>
        </div>
      </div>
    </div>
  )
}

export default Result
