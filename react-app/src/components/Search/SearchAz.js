import React, { useEffect } from 'react';
import { useDispatch, useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './Search.css'
import {getCreatures} from '../../store/creature'
import Result from '../Result/Result'

const SearchAz = () => {

  const allCreatures = useSelector(state => state.creature)
  const dispatch = useDispatch();
  // console.log("Creatures = ", allCreatures)

  let creaturesArr = []
  for (const creat in allCreatures) {
    creaturesArr.push(allCreatures[creat])
  }
  // console.log('ARRAY', creaturesArr)
  creaturesArr.sort((a, b) => {
    return a.name.localeCompare(b.name)  //Sort Function referenced from Stack Overflow
  })
  //https://stackoverflow.com/questions/8900732/sort-objects-in-an-array-alphabetically-on-one-property-of-the-array

  useEffect(() => {
    dispatch(getCreatures())
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

export default SearchAz
