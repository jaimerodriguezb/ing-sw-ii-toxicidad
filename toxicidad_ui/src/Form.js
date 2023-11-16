import useForm from "./UseForm";
import getConfig from "./Data"
import React, { useState } from "react";
import Select from "react-select";

const Form = () => {
    const { handleSubmit, status, message } = useForm();
    const {FORM_ENDPOINT} = getConfig();

    if (status === "success") {
        return (
            <>
                <div className="text-2xl">Gracias por usar este software!</div>
                <div className="text-md">{message}</div>
            </>
        );
    }

    if (status === "error") {
        return (
            <>
                <div className="text-2xl">Something bad happened!</div>
                <div className="text-md">{message}</div>
            </>
        );
    }

    return (
        <form
            action={FORM_ENDPOINT}
            onSubmit={handleSubmit}
            method="GET"
        >
            <div className="pt-0 mb-3">
                <textarea
                    type="text"
                    placeholder="Comentario"
                    name="Comentario"
                    className="focus:outline-none focus:ring relative w-full px-3 py-3 text-sm text-gray-600 placeholder-gray-400 bg-white border-0 rounded shadow outline-none"
                    required
                />
            </div>
            
            {status !== "loading" && (
                <div className="pt-0 mb-3">
                    <button
                        className="active:bg-blue-600 hover:shadow-lg focus:outline-none px-6 py-3 mb-1 mr-1 text-sm font-bold text-white uppercase transition-all duration-150 ease-linear bg-red-500 rounded shadow outline-none"
                        type="submit"
                    >
                       Medir Toxicidad
                    </button>
                </div>
            )}
        </form>
    );
};

export default Form;