import React from 'react';
import { useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import {useLocation} from 'react-router-dom'
import './Search.css'
// import {getCreatures} from '../../store/creature'
import Result from '../Result/Result'
import Pagination from '../Pagination/Pagination'
const Search = () => {
  const query = useLocation()
  const test = query.search.slice(1)

  const allCreatures = useSelector(state => state.creature)
  let creaturesArr = []
  for (const creat in allCreatures) {

    if (allCreatures[creat].name.toLowerCase().includes(test))
      creaturesArr.push(allCreatures[creat])
  }
  
  creaturesArr.sort((a, b) => {
    return a.name.localeCompare(b.name)  //Sort Function referenced from Stack Overflow
  })
  //https://stackoverflow.com/questions/8900732/sort-objects-in-an-array-alphabetically-on-one-property-of-the-array

  // useEffect(() => {
  //   setCreatures(dispatch(getCreatures()))
  // }, [dispatch])


  // if(creaturesArr){
  //    creaturesArr.map(creature => {
      // return (
      //   <Result key={creature.id} creature={creature}/>
      // )

  // })} else{
  //     return <div> No Creatures to display!</div>
  // }




  return (
    <div>
      <Navigation />
      <div className='search__results'>
        {creaturesArr.length > 0 ?
          <div className = 'search__results'>
          {creaturesArr.length > 0 ? (
            <>
            <div>
              {/* <Navigation /> */}
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
          : <div className='null__result'>No Creature under that name.. yet!</div>
        }

      </div>
  </div>
  )
}

export default Search
