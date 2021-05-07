import React, { useState, useEffect } from 'react';
// import { NavLink, Redirect, useParams } from 'react-router-dom';
import { useDispatch, useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './Search.css'
import {getCreaturesLore} from '../../store/creature'
import Result from '../Result/Result'

const Search = () => {

  const allCreatures = useSelector(state => state.creature)
  const dispatch = useDispatch();
  const [creatures, setCreatures] = useState({})
  console.log("Creatures = ", allCreatures)

  let creaturesArr = []
  for (const creat in allCreatures) {
    creaturesArr.push(allCreatures[creat])
  }
  console.log('ARRAY', creaturesArr)

  useEffect(() => {
    setCreatures(dispatch(getCreaturesLore()))
  }, [dispatch])



  return (
    <div>
      <Navigation />
      <div className='search__results'>
        {creaturesArr.map(creature => {
          return (
            <Result key={creature.id} creature={creature}/>
          )
        })}
      </div>
    </div>
  )
}

export default Search
