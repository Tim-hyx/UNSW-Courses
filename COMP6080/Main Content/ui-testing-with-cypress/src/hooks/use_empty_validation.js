function useEmptyValidation(input) {
  return (
    input !== null &&
    input !== undefined &&
    input.length > 0
  );
}

export default useEmptyValidation;
