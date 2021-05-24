import React from 'react';
import {useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './Search.css'
import Result from '../Result/Result'

const SearchLore = () => {

  const allCreatures = useSelector(state => state.creature)
  const allTags = useSelector(state => state.tag)

  // console.log("Creatures = ", allCreatures)

  let creaturesArr = []
  for (const creat in allCreatures) {
    if (allCreatures[creat].tag_id === allTags[0].id)
      creaturesArr.push(allCreatures[creat])
  }
  // console.log('ARRAY', creaturesArr)
  creaturesArr.sort((a, b) => {
    return a.name.localeCompare(b.name)  //Sort Function referenced from Stack Overflow
  })
  //https://stackoverflow.com/questions/8900732/sort-objects-in-an-array-alphabetically-on-one-property-of-the-array


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

export default SearchLore
