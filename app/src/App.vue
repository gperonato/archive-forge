<template>
  <div id="app">
    <div class="container">
      <div class="card">
        <div class="card-content">
          <img alt="Logo" class="logo" src="/forge.png" />

          <div class="content has-text-left">
            <h2>Archive-Forge</h2>

            <p id="overview">
              This is a prototype app developed at an <a href="https://www.ord-hackathon.ch/">Open Research Data Hackathon</a> which packages data according to <a href="https://frictionlessdata.io/specs/data-package/">Frictionless Data</a> specifications interactively in the web browser. This front-end is technically inspired by and uses the same libraries as the existing <a href="https://create.frictionlessdata.io/">Create tool</a>. For more details see the <a href="https://github.com/gperonato/archive-forge">README</a>.
            </p>

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
              ORD Hackathon
            </a>
          </p>
          <p class="card-footer-item">
            <a target="_blank" style="font-weight:bold" href="https://github.com/gperonato/archive-forge">
              Source code
            </a>
          </p>
        </footer>
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

.logo {
  height: 90px;
  margin-top: -20px;
  float: right;
}
</style>
