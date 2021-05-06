import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch, useParams } from "react-router-dom";
import { useDispatch } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import { authenticate } from "./store/session";
import LandingPage from './components/LandingPage/LandingPage'
import MainPage from './components/MainPage/MainPage'
import Creature from "./components/Creature/Creature";

function App() {
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);
  const [creature, setCreature] = useState()
  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }


  return (
    <BrowserRouter>
      {/* <NavBar setAuthenticated={setAuthenticated} /> */}
      <Switch>
        <Route path="/" exact={true}>
          <LandingPage />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/creatures" exact={true}>
          <MainPage />
        </Route>
        <Route path="/creatures/:creatureId" exact={true}>
          <Creature creature={creature}/>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
