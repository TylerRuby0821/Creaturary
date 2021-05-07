import React, { useState} from 'react';
import { NavLink, Redirect } from 'react-router-dom';
import { useSelector } from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './MainPage.css'


const MainPage = () => {

  const user = useSelector(state => state.session.user)
  const [search, setSearch] = useState('')
  // const dispatch = useDispatch()


  return (
    <div>
      {(user) ?
        <div className='main__container'>
          <Navigation />
          {/* <div className='positional__helper'> */}
            <div className='main__search--container'>
              <p className='main__search--header'>Peak behind the curtain...</p>
              <form >
                <input
                  className='main__search--input'
                  placeholder='Search...'
                  value=''
                  onChange={(e) => setSearch(e.target.value)}
                  ></input>
              </form>
            </div>
          {/* </div> */}
          <div className='main__body'>
            <div className='main__body--lore'>
              <NavLink to='/creatures/lore'>
                <i  class="fas fa-book"></i>
                <div className='book__text'>Lore</div>
              </NavLink>
            </div>
            <div className='main__body--az'>
              <NavLink to='/creatures/a-z'>
                <i class="fas fa-book"></i>
                <div className='book__text'>A-Z</div>
              </NavLink>
            </div>
            <div className='main__body--custom'>
              <NavLink to='/creatures/custom'>
                <i class="fas fa-book"></i>
                <div className='book__text'>Custom</div>
              </NavLink>
            </div>
          </div>
        </div>
        : Redirect('/')}
    </div>
  )
}

export default MainPage
