import React from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from "react-redux";
import './Creature.css'
import Navigation from '../Naviagtion/Navigation';



const Creature = () => {

  const allCreatures = useSelector(state => state.creature)
  // console.log('ALL CREATURES',allCreatures)
  const { creatureId } = useParams();
  // console.log(allCreatures[0].name)
  let creature = {};
  for (const creat in allCreatures) {
    // console.log("CREAT", allCreatures[creat].id)
    if (allCreatures[creat].id === parseInt(creatureId)){
      creature = {...allCreatures[creat]}

   }
  }

  const allTags = useSelector(state => state.tag)
  // console.log('ALL TAGS', allTags)
  let tag = {};
  for (const t in allTags) {
    // console.log("T------->", allTags[t].type)
    // console.log('CREATURE', creature)
    if (allTags[t].id === creature.tag_id){
      tag = {...allTags[t]}
    }
  }
  // console.log('TAG----->', tag)
  // console.log(creature)
  // console.log(creature)
  // const dispatch = useDispatch()
  // allCreatures.forEach(creat => {
  //   if (creature.id === creatureId){
  //      creature = creat
  //   }
  // });
  // const creatures = useSelector(state => state.creature)
  // console.log("CREATURES", creatures)
  // useEffect(() => {
  //   (async () => {
  //       const creat = await dispatch(getCreature(creatureId))
  //       setcurrCreature(creat)
  //   })()

  // }, [creatureId, dispatch])

  return (
    <div>
      <Navigation />
      {/* Thumbnail */}
      <div className='main__body--creature'>
        <span className='creature__name'>{creature.name}</span>
        {tag.type === 'Custom' ? <span className='creature__tag--Custom'>{tag.type}</span> : <span className='creature__tag--Lore'>{tag.type}</span> }
        {/* <span className='creature__tag'>{tag.type}</span> */}
        <div className='creature__decription'>{creature.description}</div>
      </div>
    </div>
    )
}

export default Creature;
