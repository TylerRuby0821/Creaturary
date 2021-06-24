import React from 'react';
import { NavLink} from 'react-router-dom';
import { useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './MainPage.css'
import Result from '../Result/Result'
import Pagination from '../Pagination/Pagination';

const MainPage = () => {

  const favorites = useSelector(state => state.favorite)

  let favArr = []
  for (const fav in favorites) {
     favArr.push(favorites[fav])
  }

  favArr.sort((a, b) => {
    return a.name.localeCompare(b.name)  //Sort Function referenced from Stack Overflow
  })
  //https://stackoverflow.com/questions/8900732/sort-objects-in-an-array-alphabetically-on-one-property-of-the-array

  return (
    <div>
      {/* {(user) ? */}
        <div className='main__container'>
          <Navigation />
          {/* <div className='positional__helper'> */}
            <div className='main__search--container'>

            </div>
          {/* </div> */}
          <p className='main__search--header'>Peak behind the curtain...</p>
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
          <div className='fav__container'>
            <div className='fav__header'> My Favorites:</div>
            <div className='fav__results'>
              {favArr.length > 0 ? (
                <div className='fav__results--map'>
                  <Pagination
                    data = {favArr}
                    Result = {Result}
                    title = ''
                    pagelimit = {5}
                    creatures ={4}
                  />
                </div>
              ) : (
                <h1> No Creatures to show!</h1>
              )}

            </div>
          </div>
        </div>
        {/* : Redirect('/')} */}
    </div>
  )
}

export default MainPage
