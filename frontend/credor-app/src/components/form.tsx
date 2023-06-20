import { FieldValues, useForm } from "react-hook-form";
import { useQuery, useMutation } from "react-query";
import { getForm } from "../api/queries";
import { createResponse } from "../api/mutations";
import { Responses, Response } from "../types";

export const Form = () => {
  const { register, handleSubmit } = useForm();
  const onSubmit = (data: FieldValues) => {
    const entries = Object.entries(data)
    const responses: Responses = {
      responses: entries.map(([key, value]) => ({key, value}))
      
    }
    mutate(responses)
  }

  const { data } = useQuery("getForm", () => getForm(), {
    onSuccess: () => {
      console.log("sucess");
    },
  });
  const { mutate } =
    useMutation(createResponse, {
      onSuccess: () => {
        setTimeout(() => {
          console.log("success");
        }, 2000);
      },
    }) || {};

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {data
        ? data.map((field) => (
            <input
              {...register(field.name)}
              key={field.name}
              type={field.type}
              placeholder={field.name}
            />
          ))
        : "loading"}

      <button type="submit">Send</button>
    </form>
  );
};
