// .eslintrc.js

module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:jest/recommended',
  ],
  parserOptions: {
    ecmaVersion: 12,
  },
  plugins: [
    'jest',
  ],
  rules: {
    'import/extensions': ['error', 'ignorePackages', {
      js: 'never', // Allow import of .js files without extension
    }],
  },
};
