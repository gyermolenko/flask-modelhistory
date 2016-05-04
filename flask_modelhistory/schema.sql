CREATE TABLE IF NOT EXISTS history
(
  id SERIAL PRIMARY KEY,
  date timestamp with time zone NOT NULL DEFAULT now(),
  user_id bigint default NULL ,
  object_type varchar(32) NOT NULL,
  object_id bigint NOT NULL,
  data json NOT NULL
);

CREATE INDEX object_id_idx ON history (object_id);
CREATE INDEX object_type_idx ON history (object_type);
