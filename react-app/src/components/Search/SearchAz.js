import React from 'react';
import {useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './Search.css'
import Pagination from '../Pagination/Pagination'
import Result from '../Result/Result'

const SearchAz = () => {

  const allCreatures = useSelector(state => state.creature)

  let creaturesArr = []
  for (const creat in allCreatures) {
    creaturesArr.push(allCreatures[creat])
  }
  creaturesArr.sort((a, b) => {
    return a.name.localeCompare(b.name)  //Sort Function referenced from Stack Overflow
  })
  //https://stackoverflow.com/questions/8900732/sort-objects-in-an-array-alphabetically-on-one-property-of-the-array


  return (
  //   <div>
  //     <Navigation />
  //     <div className='search__results'>
  //       {creaturesArr.map(creature => {
  //         return (
  //           <Result key={creature.id} creature={creature}/>
  //         )
  //       })}
  //     </div>
  // </div>
  <div className = 'search__results'>
      {creaturesArr.length > 0 ? (
        <>
        <div>
          <Navigation />
        </div>
        <div>
          <Pagination
            data = {creaturesArr}
            Result = {Result}
            title = 'Creatures'
            pagelimit = {5}
            creatures ={6}
          />
        </div>
        </>
      ) : (
        <h1> No Creatures to show!</h1>
      )}
      {/* )}
      <div className='search__results'>
        {creaturesArr.map(creature => {
          return (
            <Result key={creature.id} creature={creature}/>
          )
        })} */}
      {/* </div> */}
    </div>
  )
}

export default SearchAz
