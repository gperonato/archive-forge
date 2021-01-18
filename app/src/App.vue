<template>
  <div id="app">
    <div class="container">
      <div class="card">
        <div class="card-content">
          <div class="content has-text-left">
            <ArchiveForge
              chan="https://github.com/gperonato/archive-forge/issues"
            />
          </div>
        </div>

        <footer class="card-footer">
          <p class="card-footer-item">
            <a target="_blank" href="https://frictionlessdata.io">
              Frictionless Data
            </a>
          </p>
          <p class="card-footer-item">
            <a target="_blank" href="https://www.ord-hackathon.ch/">
              ORD Hackathon 2020
            </a>
          </p>
        </footer>

        <div class="card-image mt-5">
          <img
            alt="Logo"
            src="https://raw.githubusercontent.com/gperonato/archive-forge/main/images/chem.png"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArchiveForge from "./components/ArchiveForge";

export default {
  name: "App",
  components: {
    ArchiveForge,
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
