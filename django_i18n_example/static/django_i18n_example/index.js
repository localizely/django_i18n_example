function translateInJs(objectsCount) {
    const simpleString = gettext('Simple string');

    const pluralFormat = ngettext('There is %(count)s object', 'There are %(count)s objects', objectsCount);
    const pluralString = interpolate(pluralFormat, { count: objectsCount }, true);

    document.getElementById('js-simple-string').innerHTML = simpleString;
    document.getElementById('js-plural-string').innerHTML = pluralString;
}