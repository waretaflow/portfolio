<template>
  <v-app>

    <Header/>

    <v-main>
      <v-row>
        <v-col
          cols="12"
          sm="12"
        >
          <h1>スケジュール調整</h1>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          cols="12"
          sm="10"
        >
          <Calendars/>
        </v-col>

        <v-col
          cols="12"
          sm="2"
        >
          <SideNav/>
        </v-col>

      </v-row>
      
    </v-main>
  </v-app>
</template>

<script>
import Header from './components/Header';
import Calendars from './components/Calendars';
import SideNav from './components/SideNav';

export default {
  name: 'App',

  components: {
    Header,
    Calendars,
    SideNav,
  },

  data: () => ({
    //
  }),
};
</script>
