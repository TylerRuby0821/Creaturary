import React from 'react';
import { NavLink } from 'react-router-dom';
import './Result.css'

const Result = ({creature}) => {
  // console.log('CREATURE', creature)
  return (
    <div className='spacer'>
      <div className='main__container'>
        <div className='result__container'>
          <NavLink to={`/creatures/${creature.id}`} className='result__link'>
            <div className='result__thumbnail'>{/*Thumbnail*/}</div>
            <div className='result__name'>{creature.name}</div>
            <div className='result__description'>{creature.description}</div>
          </NavLink>
        </div>
      </div>
    </div>
  )
}

export default Result
