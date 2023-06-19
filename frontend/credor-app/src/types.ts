export type Response = {
  key: string;
  value: string | number;
};

export type Responses = ResultList<"responses", Response>;

export type ProposalField = {
  name: string;
  type: string | number;
  nullable: boolean;
  order: number;

};

export type ProposalFields = ResultList<"fields", ProposalField>;

export type ResultList<K extends string, T> = {
  [P in K]: T[];
};
