import React from 'react';
import { NavLink } from 'react-router-dom';
import Navigation from '../Naviagtion/Navigation'

const MainPage = () => {

  return (
    <div className='main__container'>
      <Navigation />
      <div className='main__body'>
        <div>A - Z</div>
        <div> Lore </div>
        <div> Custom</div>
      </div>
    </div>

  )
}

export default MainPage
