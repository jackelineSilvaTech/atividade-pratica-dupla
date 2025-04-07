/**
 * Retorna index da primeira ocorrência de 'needle' em 'haystack', se não for encontrada, irá retornar -1.
 * 
 * Exemplo 1.: strStr("testandobusca", "ndo") // retorna 5;
 * Exemplo 2.: strStr("testandobusca", "palavra") // retorna -1;
 * 
 * @param {string} haystack string na qual 'needle' será buscada
 * @param {string} needle string a ser buscada
 * @return {number} index da primeira ocorrência de 'needle' em 'haystack' ou -1
 */
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};