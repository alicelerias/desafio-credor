import { QueryClientProvider, QueryClient } from "react-query"
import { Form } from "./components/form";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
})


function App() {

 
  return (
    <QueryClientProvider client={queryClient}>
      <Form />
    </QueryClientProvider>
  );
}

export default App;
