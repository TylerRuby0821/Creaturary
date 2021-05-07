import React, { useState, useEffect } from 'react';
// import { NavLink, Redirect, useParams } from 'react-router-dom';
import { useDispatch} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './Search.css'
import {getCreaturesLore} from '../../store/creature'

const Search = () => {

  const dispatch = useDispatch();
  const [creatures, setCreatures] = useState({})

  useEffect(() => {
    setCreatures(dispatch(getCreaturesLore()))
  }, [creatures, dispatch])



  return (
    <div>
      <Navigation />
    </div>
  )
}

export default Search
