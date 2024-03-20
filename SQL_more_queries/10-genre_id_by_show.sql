-- Sélectionne le titre des émissions de télévision et les identifiants de genre associés
-- Jointure entre les tables tv_shows et tv_show_genres sur les clés étrangères id et tv_show_id respectivement
-- Les émissions de télévision sont liées à leurs genres correspondants
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
-- Trie les résultats par titre de l'émission de télévision et identifiant de genre
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;