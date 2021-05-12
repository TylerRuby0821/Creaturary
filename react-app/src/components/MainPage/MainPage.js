import React, { useState} from 'react';
import { NavLink, Redirect, useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './MainPage.css'
import {getCreaturesSearch} from '../../store/creature'


const MainPage = () => {

  const user = useSelector(state => state.session.user)
  const [search, setSearch] = useState('')
  const dispatch = useDispatch()
  const history = useHistory()

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('SEARCH RESULT', search)
    dispatch(getCreaturesSearch(search))
    history.push('/creatures/search')
  }

  return (
    <div>
      {(user) ?
        <div className='main__container'>
          <Navigation />
          {/* <div className='positional__helper'> */}
            <div className='main__search--container'>
              <p className='main__search--header'>Peak behind the curtain...</p>
              <form onSubmit = {handleSubmit}>
                <input
                  className='main__search--input'
                  placeholder='Search...'
                  onChange={(e) => setSearch(e.target.value)}

                  ></input>
                  <button className='search__button'><i className="fas fa-search"></i></button>
              </form>
            </div>
          {/* </div> */}
          <div className='main__body'>
            <div className='main__body--lore'>
              <NavLink to='/creatures/lore'>
                <i className="fas fa-book"></i>
                <div className='book__text'>Lore</div>
              </NavLink>
            </div>
            <div className='main__body--az'>
              <NavLink to='/creatures/a-z'>
                <i className="fas fa-book"></i>
                <div className='book__text'>A-Z</div>
              </NavLink>
            </div>
            <div className='main__body--custom'>
              <NavLink to='/creatures/custom'>
                <i className ="fas fa-book"></i>
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
