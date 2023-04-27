var path = require("path")

module.exports = {
  entry: path.join(__dirname, "leadmanager/frontend/src/index"),
  output: {
    path: path.join(__dirname, "leadmanager/frontend/static/frontend"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
}