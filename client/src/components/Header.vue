<template>
  <div>
      <v-app-bar
        color="gray accent-4"
        dark
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
  
        <v-toolbar-title>Renのさいと</v-toolbar-title>
  
        <div class="flex-grow-1"></div>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon v-on="on">
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>

      </v-app-bar>
  </div>
</template>

<script>
  export default {
    name: 'Header',
  }
</script>
