import React from 'react';
import { NavLink, Redirect } from 'react-router-dom';
import { useSelector } from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './MainPage.css'

const MainPage = () => {

  const user = useSelector(state => state.session.user)

  return (
    <div>
      {(user) ?
        <div className='main__container'>
          <Navigation />
          <div className='positional__helper'>
            <div className='main__search--container'>
              <p className='main__search--header'>Peak behind the curtain...</p>
              <input className='main__search--input'></input>
            </div>
          </div>
          <div className='main__body'>
            <div className='main__body--lore'>
              <i class="fas fa-book"></i>
              <div className='book__text'>Lore</div>
            </div>
            <div className='main__body--az'>
              <i class="fas fa-book"></i>
              <div className='book__text'>A-Z</div>
            </div>
            <div className='main__body--custom'>
              <i class="fas fa-book"></i>
              <div className='book__text'>Custom</div>
            </div>
          </div>
        </div>
        : Redirect('/')}
    </div>
  )
}

export default MainPage
